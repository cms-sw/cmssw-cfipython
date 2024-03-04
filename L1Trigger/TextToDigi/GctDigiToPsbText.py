import FWCore.ParameterSet.Config as cms

def GctDigiToPsbText(**kwargs):
  mod = cms.EDAnalyzer('GctDigiToPsbText',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
