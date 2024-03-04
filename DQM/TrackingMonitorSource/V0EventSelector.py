import FWCore.ParameterSet.Config as cms

def V0EventSelector(**kwargs):
  mod = cms.EDFilter('V0EventSelector',
    vertexCompositeCandidates = cms.InputTag('generalV0Candidates', 'Kshort'),
    minCandidates = cms.uint32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
