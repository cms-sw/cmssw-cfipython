import FWCore.ParameterSet.Config as cms

def HLTGetRaw(*args, **kwargs):
  mod = cms.EDAnalyzer('HLTGetRaw',
    RawDataCollection = cms.InputTag('rawDataCollector'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
