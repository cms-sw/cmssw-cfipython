import FWCore.ParameterSet.Config as cms

def Run3ScoutingVertexToRecoVertexProducer(*args, **kwargs):
  mod = cms.EDProducer('Run3ScoutingVertexToRecoVertexProducer',
    src = cms.InputTag('hltScoutingPrimaryVertexPacker', 'primaryVtx'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
