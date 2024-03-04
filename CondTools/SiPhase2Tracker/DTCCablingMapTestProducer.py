import FWCore.ParameterSet.Config as cms

def DTCCablingMapTestProducer(**kwargs):
  mod = cms.EDAnalyzer('DTCCablingMapTestProducer',
    iovBeginTime = cms.uint64(1),
    record = cms.string('TrackerDetToDTCELinkCablingMap'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
