import FWCore.ParameterSet.Config as cms

def L3MuonCandidateProducerFromMuons(**kwargs):
  mod = cms.EDProducer('L3MuonCandidateProducerFromMuons',
    InputObjects = cms.InputTag('hltL3Muons'),
    DisplacedReconstruction = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
