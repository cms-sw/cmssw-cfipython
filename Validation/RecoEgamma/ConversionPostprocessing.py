import FWCore.ParameterSet.Config as cms

def ConversionPostprocessing(**kwargs):
  mod = cms.EDAnalyzer('ConversionPostprocessing',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
