import FWCore.ParameterSet.Config as cms

def Primary4DVertexHarvester(*args, **kwargs):
  mod = cms.EDProducer('Primary4DVertexHarvester',
    folder = cms.string('MTD/Vertices/'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
