import FWCore.ParameterSet.Config as cms

def DiMuonValidation(*args, **kwargs):
  mod = cms.EDAnalyzer('DiMuonValidation',
    compressionSettings = cms.untracked.int32(-1),
    eBeam = cms.double(3500),
    TkTag = cms.string('ALCARECOTkAlZMuMu'),
    Pair_mass_min = cms.double(60),
    Pair_mass_max = cms.double(120),
    Pair_mass_nbins = cms.int32(120),
    Pair_etaminpos = cms.double(-2.4),
    Pair_etamaxpos = cms.double(2.4),
    Pair_etaminneg = cms.double(-2.4),
    Pair_etamaxneg = cms.double(2.4),
    Variable_CosThetaCS_xmin = cms.double(-1),
    Variable_CosThetaCS_xmax = cms.double(1),
    Variable_CosThetaCS_nbins = cms.int32(20),
    Variable_DeltaEta_xmin = cms.double(-4.8),
    Variable_DeltaEta_xmax = cms.double(4.8),
    Variable_DeltaEta_nbins = cms.int32(20),
    Variable_EtaMinus_xmin = cms.double(-2.4),
    Variable_EtaMinus_xmax = cms.double(2.4),
    Variable_EtaMinus_nbins = cms.int32(12),
    Variable_EtaPlus_xmin = cms.double(-2.4),
    Variable_EtaPlus_xmax = cms.double(2.4),
    Variable_EtaPlus_nbins = cms.int32(12),
    Variable_PhiCS_xmin = cms.double(-1.5707963267948966),
    Variable_PhiCS_xmax = cms.double(1.5707963267948966),
    Variable_PhiCS_nbins = cms.int32(20),
    Variable_PhiMinus_xmin = cms.double(-3.1415926535897931),
    Variable_PhiMinus_xmax = cms.double(3.1415926535897931),
    Variable_PhiMinus_nbins = cms.int32(16),
    Variable_PhiPlus_xmin = cms.double(-3.1415926535897931),
    Variable_PhiPlus_xmax = cms.double(3.1415926535897931),
    Variable_PhiPlus_nbins = cms.int32(16),
    Variable_PairPt_xmin = cms.double(0),
    Variable_PairPt_xmax = cms.double(100),
    Variable_PairPt_nbins = cms.int32(100),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
