import FWCore.ParameterSet.Config as cms

def HcalIsoTrackAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalIsoTrackAnalyzer',
    momentumLow = cms.double(40),
    momentumHigh = cms.double(60),
    useRaw = cms.untracked.int32(0),
    dataType = cms.untracked.int32(0),
    unCorrect = cms.untracked.int32(0),
    fillInRange = cms.untracked.bool(False),
    isoTrackVarLabel = cms.InputTag('alcaHcalIsotrkProducer', 'HcalIsoTrack'),
    isoTrackEvtLabel = cms.InputTag('alcaHcalIsotrkProducer', 'HcalIsoTrackEvent'),
    debugEvents = cms.vint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
