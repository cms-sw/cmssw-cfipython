import FWCore.ParameterSet.Config as cms

def GBRWrapperMaker(**kwargs):
  mod = cms.EDAnalyzer('GBRWrapperMaker',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
