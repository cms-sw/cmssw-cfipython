import FWCore.ParameterSet.Config as cms

def HiFJRhoFlowModulationProducer(**kwargs):
  mod = cms.EDProducer('HiFJRhoFlowModulationProducer',
    minPfCandidatesPerEvent = cms.int32(100),
    doEvtPlane = cms.bool(False),
    EvtPlane = cms.InputTag('hiEvtPlane'),
    doJettyExclusion = cms.bool(False),
    exclusionRadius = cms.double(0.4),
    doFreePlaneFit = cms.bool(False),
    jetTag = cms.InputTag('ak4PFJetsForFlow'),
    pfCandSource = cms.InputTag('packedPFCandidates'),
    evtPlaneLevel = cms.int32(0),
    pfCandidateEtaCut = cms.double(1),
    pfCandidateMinPtCut = cms.double(0.3),
    pfCandidateMaxPtCut = cms.double(3),
    firstFittedVn = cms.int32(2),
    lastFittedVn = cms.int32(3),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
