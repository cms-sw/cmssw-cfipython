import FWCore.ParameterSet.Config as cms

def Run3ScoutingElectronBestTrackProducer(*args, **kwargs):
  mod = cms.EDProducer('Run3ScoutingElectronBestTrackProducer',
    Run3ScoutingElectron = cms.InputTag('hltScoutingEgammaPacker'),
    TrackPtMin = cms.vdouble(
      0,
      0
    ),
    TrackChi2OverNdofMax = cms.vdouble(
      9999,
      9999
    ),
    RelativeEnergyDifferenceMax = cms.vdouble(
      9999,
      9999
    ),
    DeltaPhiMax = cms.vdouble(
      9999,
      9999
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
