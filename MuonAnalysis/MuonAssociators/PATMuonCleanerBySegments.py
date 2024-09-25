import FWCore.ParameterSet.Config as cms

def PATMuonCleanerBySegments(*args, **kwargs):
  mod = cms.EDProducer('PATMuonCleanerBySegments',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
