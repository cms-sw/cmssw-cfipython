import FWCore.ParameterSet.Config as cms

def HLTGetRaw(**kwargs):
  mod = cms.EDAnalyzer('HLTGetRaw',
    RawDataCollection = cms.InputTag('rawDataCollector'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
