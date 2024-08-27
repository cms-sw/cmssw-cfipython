import FWCore.ParameterSet.Config as cms

def PATMuonCleanerBySegments(**kwargs):
  mod = cms.EDProducer('PATMuonCleanerBySegments',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
