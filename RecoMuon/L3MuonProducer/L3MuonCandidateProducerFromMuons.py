import FWCore.ParameterSet.Config as cms

def L3MuonCandidateProducerFromMuons(*args, **kwargs):
  mod = cms.EDProducer('L3MuonCandidateProducerFromMuons',
    InputObjects = cms.InputTag('hltL3Muons'),
    DisplacedReconstruction = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
