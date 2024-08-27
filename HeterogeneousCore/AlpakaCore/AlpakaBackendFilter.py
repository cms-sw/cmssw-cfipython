import FWCore.ParameterSet.Config as cms

def AlpakaBackendFilter(**kwargs):
  mod = cms.EDFilter('AlpakaBackendFilter',
    producer = cms.InputTag('alpakaBackendProducer', 'backend'),
    backends = cms.vstring('SerialSync'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
