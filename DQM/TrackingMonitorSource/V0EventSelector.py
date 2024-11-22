import FWCore.ParameterSet.Config as cms

def V0EventSelector(*args, **kwargs):
  mod = cms.EDFilter('V0EventSelector',
    vertexCompositeCandidates = cms.InputTag('generalV0Candidates', 'Kshort'),
    minCandidates = cms.uint32(1),
    massMin = cms.double(0),
    massMax = cms.double(1.7976931348623157e+308),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
