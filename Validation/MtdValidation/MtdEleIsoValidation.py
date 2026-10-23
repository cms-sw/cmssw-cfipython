import FWCore.ParameterSet.Config as cms

def MtdEleIsoValidation(*args, **kwargs):
  mod = cms.EDProducer('MtdEleIsoValidation',
    folder = cms.string('MTD/ElectronIso'),
    inputTagG = cms.InputTag('generalTracks'),
    inputTag_vtx = cms.InputTag('offlinePrimaryVertices4D'),
    inputEle_EB = cms.InputTag('gedGsfElectrons'),
    inputEle_EE = cms.InputTag('ecalDrivenGsfElectronsHGC'),
    TPtoRecoTrackAssoc = cms.InputTag('trackingParticleRecoTrackAsssociation'),
    t0PID = cms.InputTag('tofPID', 't0'),
    sigmat0PID = cms.InputTag('tofPID', 'sigmat0'),
    trackMVAQual = cms.InputTag('mtdTrackQualityMVA', 'mtdQualMVA'),
    trackMinimumPt = cms.double(1),
    trackMinimumEta = cms.double(1.5),
    trackMaximumEta = cms.double(3.2),
    rel_iso_cut = cms.double(0.08),
    optionTrackMatchToPV = cms.bool(False),
    option_dtToTrack = cms.bool(True),
    option_plots = cms.bool(False),
    min_dR_cut = cms.double(0.01),
    max_dR_cut = cms.double(0.3),
    min_pt_cut_EB = cms.double(0.7),
    min_pt_cut_EE = cms.double(0.4),
    max_dz_cut_EB = cms.double(0.5),
    max_dz_cut_EE = cms.double(0.5),
    max_dz_vtx_cut = cms.double(0.5),
    max_dxy_vtx_cut = cms.double(0.2),
    min_strip_cut = cms.double(0.01),
    min_track_mtd_mva_cut = cms.double(0.5),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
