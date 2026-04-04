;; AIP-HSD Security Logic Rule Engine (Clojure)
;; Used for complex, high-level policy evaluation using functional paradigms.

(ns aiphsd.rules
  (:require [clojure.string :as str]))

(defn evaluate-threat-tactic
  "Evaluates the risk of a detected tactic based on historical severity data."
  [tactic]
  (let [severity-map {"Data Exfiltration" 0.95
                      "Lateral Movement" 0.8
                      "Resource Hijacking" 0.7
                      "Initial Access" 0.5}]
    (get severity-map tactic 0.1)))

(defn should-auto-remediate?
  "Determines if an automated action should be triggered."
  [risk-score confidence-score]
  (and (> risk-score 0.8) (> confidence-score 0.85)))

(defn -main
  [& args]
  (println "AIP-HSD Clojure Rule Engine: Evaluating Tactic 'Data Exfiltration'...")
  (let [risk (evaluate-threat-tactic "Data Exfiltration")]
    (println "Calculated Risk Factor:" risk)
    (println "Automated Remediation Authorized:" (should-auto-remediate? risk 0.9))))

(-main)
