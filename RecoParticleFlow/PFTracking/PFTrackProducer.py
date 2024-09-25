import FWCore.ParameterSet.Config as cms

def PFTrackProducer(*args, **kwargs):
  mod = cms.EDProducer('PFTrackProducer',
    TrackQuality = cms.string('highPurity'),
    UseQuality = cms.bool(True),
    GsfTrackModuleLabel = cms.InputTag('electronGsfTracks'),
    TkColList = cms.VInputTag('generalTracks'),
    PrimaryVertexLabel = cms.InputTag('offlinePrimaryVertices'),
    MuColl = cms.InputTag('muons1stStep'),
    TrajInEvents = cms.bool(False),
    GsfTracksInEvents = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
