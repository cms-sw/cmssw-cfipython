import FWCore.ParameterSet.Config as cms

def TripletFeaturesTableProducer(*args, **kwargs):
  mod = cms.EDProducer('TripletFeaturesTableProducer',
    tableName = cms.string('Triplet'),
    tripletDumpSrc = cms.InputTag('pixelTracksAlpaka'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
