import FWCore.ParameterSet.Config as cms

def EcalCompactTrigPrimProducerTest(**kwargs):
  mod = cms.EDAnalyzer('EcalCompactTrigPrimProducerTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
