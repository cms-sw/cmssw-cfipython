import FWCore.ParameterSet.Config as cms

def AlCaHcalIsotrkFilter(*args, **kwargs):
  mod = cms.EDFilter('AlCaHcalIsotrkFilter',
    momentumLow = cms.double(40),
    momentumHigh = cms.double(60),
    prescaleLow = cms.int32(1),
    prescaleHigh = cms.int32(1),
    isoTrackLabel = cms.InputTag('alcaHcalIsotrkProducer', 'HcalIsoTrack'),
    debugEvents = cms.vint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
