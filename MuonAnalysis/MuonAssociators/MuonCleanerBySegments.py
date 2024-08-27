import FWCore.ParameterSet.Config as cms

def MuonCleanerBySegments(**kwargs):
  mod = cms.EDProducer('MuonCleanerBySegments',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
