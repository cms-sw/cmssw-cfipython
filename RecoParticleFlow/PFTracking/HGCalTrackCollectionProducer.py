import FWCore.ParameterSet.Config as cms

def HGCalTrackCollectionProducer(*args, **kwargs):
  mod = cms.EDProducer('HGCalTrackCollectionProducer',
    src = cms.InputTag('pfTrack'),
    trackQuality = cms.string('highPurity'),
    useIterativeTracking = cms.bool(True),
    DPtOverPtCuts_byTrackAlgo = cms.vdouble(
      10,
      10,
      10,
      10,
      10,
      5
    ),
    NHitCuts_byTrackAlgo = cms.vuint32(
      3,
      3,
      3,
      3,
      3,
      3
    ),
    hgcalGeometryNames = cms.PSet(
      HGC_ECAL = cms.string('HGCalEESensitive')
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
