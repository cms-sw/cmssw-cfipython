import FWCore.ParameterSet.Config as cms

def PFBlockProducer(**kwargs):
  mod = cms.EDProducer('PFBlockProducer',
    verbose = cms.untracked.bool(False),
    debug = cms.untracked.bool(False),
    elementImporters = cms.VPSet(
      cms.PSet(
        gsfsAreSecondary = cms.bool(False),
        importerName = cms.string('GSFTrackImporter'),
        source = cms.InputTag('pfTrackElec'),
        superClustersArePF = cms.bool(True)
      ),
      cms.PSet(
        importerName = cms.string('ConvBremTrackImporter'),
        source = cms.InputTag('pfTrackElec'),
        vetoEndcap = cms.bool(False)
      ),
      cms.PSet(
        hbheRecHitsTag = cms.InputTag('hbhereco'),
        importerName = cms.string('SuperClusterImporter'),
        maxSeverityHB = cms.int32(9),
        maxSeverityHE = cms.int32(9),
        maximumHoverE = cms.double(0.5),
        minPTforBypass = cms.double(100),
        minSuperClusterPt = cms.double(10),
        source_eb = cms.InputTag('particleFlowSuperClusterECAL', 'particleFlowSuperClusterECALBarrel'),
        source_ee = cms.InputTag('particleFlowSuperClusterECAL', 'particleFlowSuperClusterECALEndcapWithPreshower'),
        superClustersArePF = cms.bool(True),
        usePFThresholdsFromDB = cms.bool(False)
      ),
      cms.PSet(
        importerName = cms.string('ConversionTrackImporter'),
        source = cms.InputTag('pfConversions'),
        vetoEndcap = cms.bool(False)
      ),
      cms.PSet(
        importerName = cms.string('NuclearInteractionTrackImporter'),
        source = cms.InputTag('pfDisplacedTrackerVertex'),
        vetoEndcap = cms.bool(False)
      ),
      cms.PSet(
        DPtOverPtCuts_byTrackAlgo = cms.vdouble(
          10,
          10,
          10,
          10,
          10,
          5
        ),
        NHitCuts_byTrackAlgo = cms.vuint32(
          3,
          3,
          3,
          3,
          3,
          3
        ),
        cleanBadConvertedBrems = cms.bool(True),
        importerName = cms.string('GeneralTracksImporter'),
        muonMaxDPtOPt = cms.double(1),
        muonSrc = cms.InputTag('muons1stStep'),
        source = cms.InputTag('pfTrack'),
        trackQuality = cms.string('highPurity'),
        useIterativeTracking = cms.bool(True),
        vetoEndcap = cms.bool(False)
      ),
      cms.PSet(
        BCtoPFCMap = cms.InputTag('particleFlowSuperClusterECAL', 'PFClusterAssociationEBEE'),
        importerName = cms.string('ECALClusterImporter'),
        source = cms.InputTag('particleFlowClusterECAL')
      ),
      cms.PSet(
        importerName = cms.string('GenericClusterImporter'),
        source = cms.InputTag('particleFlowClusterHCAL')
      ),
      cms.PSet(
        importerName = cms.string('GenericClusterImporter'),
        source = cms.InputTag('particleFlowBadHcalPseudoCluster')
      ),
      cms.PSet(
        importerName = cms.string('GenericClusterImporter'),
        source = cms.InputTag('particleFlowClusterHO')
      ),
      cms.PSet(
        importerName = cms.string('GenericClusterImporter'),
        source = cms.InputTag('particleFlowClusterHF')
      ),
      cms.PSet(
        importerName = cms.string('GenericClusterImporter'),
        source = cms.InputTag('particleFlowClusterPS')
      )
    ),
    linkDefinitions = cms.VPSet(
      cms.PSet(
        linkType = cms.string('PS1:ECAL'),
        linkerName = cms.string('PreshowerAndECALLinker'),
        useKDTree  = cms.bool(True)
      ),
      cms.PSet(
        linkType = cms.string('PS2:ECAL'),
        linkerName = cms.string('PreshowerAndECALLinker'),
        useKDTree  = cms.bool(True)
      ),
      cms.PSet(
        linkType = cms.string('TRACK:ECAL'),
        linkerName = cms.string('TrackAndECALLinker'),
        useKDTree  = cms.bool(True)
      ),
      cms.PSet(
        linkType = cms.string('TRACK:HCAL'),
        linkerName = cms.string('TrackAndHCALLinker'),
        nMaxHcalLinksPerTrack = cms.int32(1),
        trajectoryLayerEntrance = cms.string('HCALEntrance'),
        trajectoryLayerExit = cms.string('HCALExit'),
        useKDTree = cms.bool(True)
      ),
      cms.PSet(
        linkType = cms.string('TRACK:HO'),
        linkerName = cms.string('TrackAndHOLinker'),
        useKDTree = cms.bool(False)
      ),
      cms.PSet(
        linkType = cms.string('ECAL:HCAL'),
        linkerName = cms.string('ECALAndHCALLinker'),
        minAbsEtaEcal = cms.double(2.5),
        useKDTree = cms.bool(False)
      ),
      cms.PSet(
        linkType = cms.string('HCAL:HO'),
        linkerName = cms.string('HCALAndHOLinker'),
        useKDTree = cms.bool(False)
      ),
      cms.PSet(
        linkType = cms.string('HFEM:HFHAD'),
        linkerName = cms.string('HFEMAndHFHADLinker'),
        useKDTree = cms.bool(False)
      ),
      cms.PSet(
        linkType = cms.string('TRACK:TRACK'),
        linkerName = cms.string('TrackAndTrackLinker'),
        useKDTree = cms.bool(False)
      ),
      cms.PSet(
        linkType = cms.string('ECAL:ECAL'),
        linkerName = cms.string('ECALAndECALLinker'),
        useKDTree = cms.bool(False)
      ),
      cms.PSet(
        linkType = cms.string('GSF:ECAL'),
        linkerName = cms.string('GSFAndECALLinker'),
        useKDTree = cms.bool(False)
      ),
      cms.PSet(
        linkType = cms.string('TRACK:GSF'),
        linkerName = cms.string('TrackAndGSFLinker'),
        useConvertedBrems = cms.bool(True),
        useKDTree = cms.bool(False)
      ),
      cms.PSet(
        linkType = cms.string('GSF:BREM'),
        linkerName = cms.string('GSFAndBREMLinker'),
        useKDTree = cms.bool(False)
      ),
      cms.PSet(
        linkType = cms.string('GSF:GSF'),
        linkerName = cms.string('GSFAndGSFLinker'),
        useKDTree = cms.bool(False)
      ),
      cms.PSet(
        linkType = cms.string('ECAL:BREM'),
        linkerName = cms.string('ECALAndBREMLinker'),
        useKDTree = cms.bool(False)
      ),
      cms.PSet(
        linkType = cms.string('GSF:HCAL'),
        linkerName = cms.string('GSFAndHCALLinker'),
        useKDTree = cms.bool(False)
      ),
      cms.PSet(
        linkType = cms.string('HCAL:BREM'),
        linkerName = cms.string('HCALAndBREMLinker'),
        useKDTree = cms.bool(False)
      ),
      cms.PSet(
        SuperClusterMatchByRef = cms.bool(True),
        linkType = cms.string('SC:ECAL'),
        linkerName = cms.string('SCAndECALLinker'),
        useKDTree = cms.bool(False)
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
