import FWCore.ParameterSet.Config as cms

def LightPFTrackProducer(*args, **kwargs):
  mod = cms.EDProducer('LightPFTrackProducer',
    TrackQuality = cms.string('highPurity'),
    UseQuality = cms.bool(True),
    TkColList = cms.VInputTag(
      'generalTracks',
      'secStep',
      'thStep'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
