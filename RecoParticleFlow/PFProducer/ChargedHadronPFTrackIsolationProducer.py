import FWCore.ParameterSet.Config as cms

def ChargedHadronPFTrackIsolationProducer(**kwargs):
  mod = cms.EDProducer('ChargedHadronPFTrackIsolationProducer',
    src = cms.InputTag('particleFlow'),
    minTrackPt = cms.double(1),
    minRawCaloEnergy = cms.double(0.5),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
