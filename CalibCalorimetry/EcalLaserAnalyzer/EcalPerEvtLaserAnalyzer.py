import FWCore.ParameterSet.Config as cms

def EcalPerEvtLaserAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalPerEvtLaserAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
