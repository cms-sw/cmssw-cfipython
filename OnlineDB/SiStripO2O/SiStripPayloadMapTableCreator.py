import FWCore.ParameterSet.Config as cms

def SiStripPayloadMapTableCreator(**kwargs):
  mod = cms.EDAnalyzer('SiStripPayloadMapTableCreator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
