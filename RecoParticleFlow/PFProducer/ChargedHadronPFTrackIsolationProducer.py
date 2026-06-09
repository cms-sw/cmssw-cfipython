import FWCore.ParameterSet.Config as cms

def ChargedHadronPFTrackIsolationProducer(*args, **kwargs):
  mod = cms.EDProducer('ChargedHadronPFTrackIsolationProducer',
    src = cms.InputTag('particleFlow'),
    minTrackPt = cms.double(1),
    minRawCaloEnergy = cms.double(0.5),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
