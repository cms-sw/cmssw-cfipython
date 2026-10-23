import FWCore.ParameterSet.Config as cms

def ConversionPostprocessing(*args, **kwargs):
  mod = cms.EDAnalyzer('ConversionPostprocessing',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
