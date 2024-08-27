import FWCore.ParameterSet.Config as cms

def OMTFPatternMaker(**kwargs):
  mod = cms.EDAnalyzer('OMTFPatternMaker',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
