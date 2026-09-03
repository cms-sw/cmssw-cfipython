import FWCore.ParameterSet.Config as cms

def TruthGraphTopologyChecker(*args, **kwargs):
  mod = cms.EDAnalyzer('TruthGraphTopologyChecker',
    rawSrc = cms.InputTag('truthGraphProducer'),
    src = cms.InputTag('truthLogicalGraphProducer'),
    failOnViolations = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
