import FWCore.ParameterSet.Config as cms

def StreamThingAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('StreamThingAnalyzer',
    product_to_get = cms.required.string,
    inChecksum = cms.untracked.string(''),
    outChecksum = cms.untracked.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
