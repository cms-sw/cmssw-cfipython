import FWCore.ParameterSet.Config as cms

def TruthBranchCandidateValidator(*args, **kwargs):
  mod = cms.EDProducer('TruthBranchCandidateValidator',
    src = cms.InputTag('truthLogicalGraphProducer'),
    hitIndex = cms.InputTag('truthLogicalGraphHitIndexProducer'),
    dirName = cms.string('TruthInfo/Offline/Candidates/'),
    recoCollections = cms.VInputTag('ticlCandidate'),
    associator = cms.string('truthBranchCandidateAssociators'),
    tracks = cms.InputTag('generalTracks'),
    trackAssociator = cms.string('allTrackToTruthBranchAssociators'),
    targetsProducer = cms.string('truthBranchTargets'),
    workingPoints = cms.vstring(
      'AdaptiveTight',
      'AdaptiveNominal'
    ),
    referenceWorkingPoint = cms.string('Fixed'),
    truthLevels = cms.vstring(
      'reconstructableFromSignal',
      'caloBoundary'
    ),
    requireHits = cms.bool(False),
    denominatorDetectors = cms.vstring(),
    dominanceLevel = cms.string('caloBoundary'),
    minLeadingTruthShare = cms.double(0.5),
    minTrackPurity = cms.double(0.75),
    energyResponseMin = cms.double(0.7),
    energyResponseMax = cms.double(1.3),
    histoBlock = cms.PSet(
      nint_pt = cms.int32(50),
      min_pt = cms.double(0),
      max_pt = cms.double(1000),
      linthresh_pt = cms.double(0.1),
      nint_eta = cms.int32(50),
      min_eta = cms.double(-4.5),
      max_eta = cms.double(4.5),
      linthresh_eta = cms.double(0),
      nint_phi = cms.int32(36),
      min_phi = cms.double(-3.2),
      max_phi = cms.double(3.2),
      linthresh_phi = cms.double(0),
      nint_energy = cms.int32(50),
      min_energy = cms.double(0),
      max_energy = cms.double(2000),
      linthresh_energy = cms.double(1),
      nint_res = cms.int32(100),
      min_res = cms.double(-1),
      max_res = cms.double(1),
      nint_res_energy = cms.int32(25),
      min_res_energy = cms.double(0),
      max_res_energy = cms.double(500),
      nint_res_eta = cms.int32(20),
      min_res_eta = cms.double(-4),
      max_res_eta = cms.double(4),
      nint_res_pt = cms.int32(15),
      min_res_pt = cms.double(0),
      max_res_pt = cms.double(150),
      etaRegions = cms.vstring('eta15to30')
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
