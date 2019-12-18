import FWCore.ParameterSet.Config as cms

particleFlow = cms.EDProducer('PFProducer',
  verbose = cms.untracked.bool(False),
  debug = cms.untracked.bool(False),
  blocks = cms.InputTag('particleFlowBlock'),
  muons = cms.InputTag('muons1stStep'),
  postMuonCleaning = cms.bool(True),
  vertexCollection = cms.InputTag('offlinePrimaryVertices'),
  useVerticesForNeutral = cms.bool(True),
  useHO = cms.bool(True),
  PFEGammaCandidates = cms.InputTag('particleFlowEGamma'),
  GedElectronValueMap = cms.InputTag('gedGsfElectronsTmp'),
  GedPhotonValueMap = cms.InputTag('gedPhotonsTmp', 'valMapPFEgammaCandToPhoton'),
  useEGammaElectrons = cms.bool(True),
  egammaElectrons = cms.InputTag('mvaElectrons'),
  useEGammaFilters = cms.bool(True),
  useProtectionsForJetMET = cms.bool(True),
  PFEGammaFiltersParameters = cms.PSet(
    electron_iso_pt = cms.double(10),
    electron_iso_mva_barrel = cms.double(-0.1875),
    electron_iso_mva_endcap = cms.double(-0.1075),
    electron_iso_combIso_barrel = cms.double(10),
    electron_iso_combIso_endcap = cms.double(10),
    electron_noniso_mvaCut = cms.double(-0.1),
    electron_missinghits = cms.uint32(1),
    electron_ecalDrivenHademPreselCut = cms.double(0.15),
    electron_maxElePtForOnlyMVAPresel = cms.double(50),
    electron_protectionsForJetMET = cms.PSet(
      maxNtracks = cms.double(3),
      maxHcalE = cms.double(10),
      maxTrackPOverEele = cms.double(1),
      maxE = cms.double(50),
      maxEleHcalEOverEcalE = cms.double(0.1),
      maxEcalEOverPRes = cms.double(0.2),
      maxEeleOverPoutRes = cms.double(0.5),
      maxHcalEOverP = cms.double(1),
      maxHcalEOverEcalE = cms.double(0.1),
      maxEcalEOverP_1 = cms.double(0.5),
      maxEcalEOverP_2 = cms.double(0.2),
      maxEeleOverPout = cms.double(0.2),
      maxDPhiIN = cms.double(0.1)
    ),
    electron_protectionsForBadHcal = cms.PSet(
      enableProtections = cms.bool(False),
      full5x5_sigmaIetaIeta = cms.vdouble(
        0.0106,
        0.0387
      ),
      eInvPInv = cms.vdouble(
        0.184,
        0.0721
      ),
      dEta = cms.vdouble(
        0.0064,
        0.01264
      ),
      dPhi = cms.vdouble(
        0.0547,
        0.0394
      )
    ),
    photon_MinEt = cms.double(10),
    photon_combIso = cms.double(10),
    photon_HoE = cms.double(0.05),
    photon_SigmaiEtaiEta_barrel = cms.double(0.0125),
    photon_SigmaiEtaiEta_endcap = cms.double(0.034),
    photon_protectionsForJetMET = cms.PSet(
      sumPtTrackIso = cms.double(4),
      sumPtTrackIsoSlope = cms.double(0.001)
    ),
    photon_protectionsForBadHcal = cms.PSet(
      solidConeTrkIsoSlope = cms.double(0.3),
      enableProtections = cms.bool(False),
      solidConeTrkIsoOffset = cms.double(10)
    )
  ),
  muon_HCAL = cms.vdouble(
    3,
    3
  ),
  muon_ECAL = cms.vdouble(
    0.5,
    0.5
  ),
  muon_HO = cms.vdouble(
    0.9,
    0.9
  ),
  PFMuonAlgoParameters = cms.PSet(
    electron_iso_pt = cms.double(10),
    electron_iso_mva_barrel = cms.double(-0.1875),
    electron_iso_mva_endcap = cms.double(-0.1075),
    electron_iso_combIso_barrel = cms.double(10),
    electron_iso_combIso_endcap = cms.double(10),
    electron_noniso_mvaCut = cms.double(-0.1),
    electron_missinghits = cms.uint32(1),
    electron_ecalDrivenHademPreselCut = cms.double(0.15),
    electron_maxElePtForOnlyMVAPresel = cms.double(50),
    electron_protectionsForJetMET = cms.PSet(
      maxNtracks = cms.double(3),
      maxHcalE = cms.double(10),
      maxTrackPOverEele = cms.double(1),
      maxE = cms.double(50),
      maxEleHcalEOverEcalE = cms.double(0.1),
      maxEcalEOverPRes = cms.double(0.2),
      maxEeleOverPoutRes = cms.double(0.5),
      maxHcalEOverP = cms.double(1),
      maxHcalEOverEcalE = cms.double(0.1),
      maxEcalEOverP_1 = cms.double(0.5),
      maxEcalEOverP_2 = cms.double(0.2),
      maxEeleOverPout = cms.double(0.2),
      maxDPhiIN = cms.double(0.1)
    ),
    electron_protectionsForBadHcal = cms.PSet(
      enableProtections = cms.bool(False),
      full5x5_sigmaIetaIeta = cms.vdouble(
        0.0106,
        0.0387
      ),
      eInvPInv = cms.vdouble(
        0.184,
        0.0721
      ),
      dEta = cms.vdouble(
        0.0064,
        0.01264
      ),
      dPhi = cms.vdouble(
        0.0547,
        0.0394
      )
    ),
    photon_MinEt = cms.double(10),
    photon_combIso = cms.double(10),
    photon_HoE = cms.double(0.05),
    photon_SigmaiEtaiEta_barrel = cms.double(0.0125),
    photon_SigmaiEtaiEta_endcap = cms.double(0.034),
    photon_protectionsForJetMET = cms.PSet(
      sumPtTrackIso = cms.double(4),
      sumPtTrackIsoSlope = cms.double(0.001)
    ),
    photon_protectionsForBadHcal = cms.PSet(
      solidConeTrkIsoSlope = cms.double(0.3),
      enableProtections = cms.bool(False),
      solidConeTrkIsoOffset = cms.double(10)
    )
  ),
  rejectTracks_Bad = cms.bool(True),
  rejectTracks_Step45 = cms.bool(True),
  usePFNuclearInteractions = cms.bool(True),
  usePFConversions = cms.bool(True),
  usePFDecays = cms.bool(False),
  dptRel_DispVtx = cms.double(10),
  iCfgCandConnector = cms.PSet(
    bCorrect = cms.bool(True),
    bCalibPrimary = cms.bool(True),
    dptRel_PrimaryTrack = cms.double(10),
    dptRel_MergedTrack = cms.double(5),
    ptErrorSecondary = cms.double(1),
    nuclCalibFactors = cms.vdouble(
      0.8,
      0.15,
      0.5,
      0.5,
      0.05
    )
  ),
  nsigma_TRACK = cms.double(1),
  pt_Error = cms.double(1),
  factors_45 = cms.vdouble(
    10,
    100
  ),
  goodTrackDeadHcal_ptErrRel = cms.double(0.2),
  goodTrackDeadHcal_chi2n = cms.double(5),
  goodTrackDeadHcal_layers = cms.uint32(4),
  goodTrackDeadHcal_validFr = cms.double(0.5),
  goodTrackDeadHcal_dxy = cms.double(0.5),
  goodPixelTrackDeadHcal_minEta = cms.double(2.3),
  goodPixelTrackDeadHcal_maxPt = cms.double(50),
  goodPixelTrackDeadHcal_ptErrRel = cms.double(1),
  goodPixelTrackDeadHcal_chi2n = cms.double(2),
  goodPixelTrackDeadHcal_maxLost3Hit = cms.int32(0),
  goodPixelTrackDeadHcal_maxLost4Hit = cms.int32(1),
  goodPixelTrackDeadHcal_dxy = cms.double(0.02),
  goodPixelTrackDeadHcal_dz = cms.double(0.05),
  pf_nsigma_ECAL = cms.double(0),
  pf_nsigma_HCAL = cms.double(1),
  pf_nsigma_HFEM = cms.double(1),
  pf_nsigma_HFHAD = cms.double(1),
  useCalibrationsFromDB = cms.bool(True),
  calibrationsLabel = cms.string(''),
  postHFCleaning = cms.bool(False),
  PFHFCleaningParameters = cms.PSet(
    minHFCleaningPt = cms.double(5),
    maxSignificance = cms.double(2.5),
    minSignificance = cms.double(2.5),
    minSignificanceReduction = cms.double(1.4),
    maxDeltaPhiPt = cms.double(7),
    minDeltaMet = cms.double(0.4)
  ),
  cleanedHF = cms.VInputTag(
    'particleFlowRecHitHF:Cleaned',
    'particleFlowClusterHF:Cleaned'
  ),
  calibHF_use = cms.bool(False),
  calibHF_eta_step = cms.vdouble(
    0,
    2.9,
    3,
    3.2,
    4.2,
    4.4,
    4.6,
    4.8,
    5.2,
    5.4
  ),
  calibHF_a_EMonly = cms.vdouble(
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1
  ),
  calibHF_a_EMHAD = cms.vdouble(
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1
  ),
  calibHF_b_HADonly = cms.vdouble(
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1
  ),
  calibHF_b_EMHAD = cms.vdouble(
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1
  ),
  resolHF_square = cms.vdouble(
    7.834401,
    0.012996,
    0
  ),
  mightGet = cms.optional.untracked.vstring
)
