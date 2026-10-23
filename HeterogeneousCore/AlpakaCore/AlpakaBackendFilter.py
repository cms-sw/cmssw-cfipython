import FWCore.ParameterSet.Config as cms

def AlpakaBackendFilter(*args, **kwargs):
  mod = cms.EDFilter('AlpakaBackendFilter',
    producer = cms.InputTag('alpakaBackendProducer', 'backend'),
    backends = cms.vstring('SerialSync'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
