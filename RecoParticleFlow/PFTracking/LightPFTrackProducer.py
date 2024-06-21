import FWCore.ParameterSet.Config as cms

def LightPFTrackProducer(**kwargs):
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
