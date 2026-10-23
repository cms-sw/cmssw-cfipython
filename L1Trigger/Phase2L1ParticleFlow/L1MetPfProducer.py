import FWCore.ParameterSet.Config as cms

def L1MetPfProducer(*args, **kwargs):
  mod = cms.EDProducer('L1MetPfProducer',
    L1PFObjects = cms.InputTag('L1PFProducer', 'l1pfCandidates'),
    maxCands = cms.int32(128),
    modelVersion = cms.string(''),
    Poly2File = cms.FileInPath('L1Trigger/Phase2L1ParticleFlow/data/met/l1met_ptphi2pxpy_poly2_v1.json'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
