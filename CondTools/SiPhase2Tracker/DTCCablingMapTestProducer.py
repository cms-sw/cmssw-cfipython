import FWCore.ParameterSet.Config as cms

def DTCCablingMapTestProducer(*args, **kwargs):
  mod = cms.EDAnalyzer('DTCCablingMapTestProducer',
    iovBeginTime = cms.uint64(1),
    record = cms.string('TrackerDetToDTCELinkCablingMap'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
