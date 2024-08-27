import FWCore.ParameterSet.Config as cms

def WriteCTPPSPixelDAQMapping(**kwargs):
  mod = cms.EDAnalyzer('WriteCTPPSPixelDAQMapping',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
