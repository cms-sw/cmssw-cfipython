import FWCore.ParameterSet.Config as cms

def EcalDAQTowerStatusAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalDAQTowerStatusAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
