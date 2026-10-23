import FWCore.ParameterSet.Config as cms

def MtdTracksHarvester(*args, **kwargs):
  mod = cms.EDProducer('MtdTracksHarvester',
    folder = cms.string('MTD/Tracks/'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
