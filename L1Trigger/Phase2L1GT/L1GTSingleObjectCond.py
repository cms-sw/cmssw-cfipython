import FWCore.ParameterSet.Config as cms

def L1GTSingleObjectCond(**kwargs):
  mod = cms.EDFilter('L1GTSingleObjectCond',
    tag = cms.required.InputTag,
    minPt = cms.optional.double,
    maxPt = cms.optional.double,
    minEta = cms.optional.double,
    maxEta = cms.optional.double,
    minPhi = cms.optional.double,
    maxPhi = cms.optional.double,
    minZ0 = cms.optional.double,
    maxZ0 = cms.optional.double,
    minScalarSumPt = cms.optional.double,
    maxScalarSumPt = cms.optional.double,
    qual = cms.vuint32(),
    minAbsEta = cms.optional.double,
    maxAbsEta = cms.optional.double,
    maxIso = cms.optional.double,
    minHwIso = cms.optional.int32,
    regionsAbsEtaLowerBounds = cms.vdouble(),
    regionsMinPt = cms.vdouble(),
    regionsMaxIso = cms.vdouble(),
    regionsQual = cms.vuint32(),
    scales = cms.PSet(
      pT_lsb = cms.required.double,
      phi_lsb = cms.required.double,
      eta_lsb = cms.required.double,
      z0_lsb = cms.required.double,
      isolation_lsb = cms.required.double,
      beta_lsb = cms.required.double,
      mass_lsb = cms.required.double,
      seed_pT_lsb = cms.required.double,
      seed_z0_lsb = cms.required.double,
      sca_sum_lsb = cms.required.double,
      sum_pT_pv_lsb = cms.required.double,
      pos_chg = cms.required.int32,
      neg_chg = cms.required.int32
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
