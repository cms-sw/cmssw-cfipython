import FWCore.ParameterSet.Config as cms

def DumpProductNames(*args, **kwargs):
  mod = cms.EDAnalyzer('DumpProductNames',
    outputFile = cms.string('product_names.json'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
