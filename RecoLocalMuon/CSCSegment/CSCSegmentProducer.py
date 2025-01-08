import FWCore.ParameterSet.Config as cms

def CSCSegmentProducer(*args, **kwargs):
  mod = cms.EDProducer('CSCSegmentProducer',
    inputObjects = cms.InputTag('csc2DRecHits'),
    algo_type = cms.int32(5),
    algo_psets = cms.required.VPSet,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
