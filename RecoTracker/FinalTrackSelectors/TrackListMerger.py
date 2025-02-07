import FWCore.ParameterSet.Config as cms

def TrackListMerger(*args, **kwargs):
  mod = cms.EDProducer('TrackListMerger',
    copyExtras = cms.untracked.bool(True),
    copyMVA = cms.bool(True),
    trackAlgoPriorityOrder = cms.required.string,
    TrackProducers = cms.VInputTag(
      '',
      ''
    ),
    MaxNormalizedChisq = cms.double(1000),
    MinPT = cms.double(0.05),
    MinFound = cms.int32(3),
    Epsilon = cms.double(-0.001),
    ShareFrac = cms.double(0.19),
    allowFirstHitShare = cms.bool(True),
    FoundHitBonus = cms.double(5),
    LostHitPenalty = cms.double(5),
    indivShareFrac = cms.vdouble(
      1,
      1
    ),
    newQuality = cms.string('confirmed'),
    setsToMerge = cms.VPSet(
    ),
    hasSelector = cms.vint32(
      0,
      0
    ),
    selectedTrackQuals = cms.VInputTag(
      '',
      ''
    ),
    mvaValueTags = cms.optional.VInputTag,
    writeOnlyTrkQuals = cms.bool(False),
    makeReKeyedSeeds = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
