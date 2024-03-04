import FWCore.ParameterSet.Config as cms

def MtdTracksHarvester(**kwargs):
  mod = cms.EDProducer('MtdTracksHarvester',
    folder = cms.string('MTD/Tracks/'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
