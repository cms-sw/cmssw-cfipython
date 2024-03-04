import FWCore.ParameterSet.Config as cms

def EcalLaserCondTools(**kwargs):
  mod = cms.EDAnalyzer('EcalLaserCondTools',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
