import FWCore.ParameterSet.Config as cms

def Primary4DVertexHarvester(**kwargs):
  mod = cms.EDProducer('Primary4DVertexHarvester',
    folder = cms.string('MTD/Vertices/'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
